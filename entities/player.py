from ursina import Entity, Vec2, Vec3, color, mouse, camera
from ursina.prefabs.first_person_controller import FirstPersonController
from entities.weapon import Weapon
from settings import PLAYER_SPEED, PLAYER_HEALTH, PLAYER_JUMP_HEIGHT, PLAYER_GRAVITY, CAMERA_POSITION, CAMERA_SENSITIVITY

class Player(FirstPersonController):
    def __init__(self):
        super().__init__()
        self.model = 'cube'  # Модель игрока
        self.color = color.blue  # Цвет игрока
        self.scale = (1, 2, 1)  # Масштаб игрока
        self.position = (0, 1, 0)  # Позиция игрока
        self.collider = 'box'  # Коллайдер для взаимодействий

        # Настройки камеры
        self.camera_pivot = Entity(parent=self)  # Точка вращения камеры
        self.camera = Entity(parent=self.camera_pivot, position=CAMERA_POSITION)  # Камера
        camera.parent = self.camera_pivot  # Привязка камеры к точке вращения
        camera.position = CAMERA_POSITION  # Позиция камеры (вид от третьего лица)
        camera.rotation = (0, 0, 0)  # Поворот камеры

        # Настройки управления
        self.mouse_sensitivity = Vec2(*CAMERA_SENSITIVITY)  # Чувствительность мыши
        self.cursor.visible = False  # Скрыть курсор
        self.gravity = PLAYER_GRAVITY
        self.jump_height = PLAYER_JUMP_HEIGHT
        self.health = PLAYER_HEALTH
        self.weapon = Weapon(parent=self)
        self.is_attacking = False
        self.is_blocking = False

    def update(self):
        self.handle_mouse_input()  # Обработка ввода мыши
        self.handle_keyboard_input()  # Обработка ввода с клавиатуры

    def handle_mouse_input(self):
        # Вращение камеры с помощью мыши
        if mouse.locked:
            self.camera_pivot.rotation_y += mouse.velocity[0] * self.mouse_sensitivity[0]
            self.camera_pivot.rotation_x -= mouse.velocity[1] * self.mouse_sensitivity[1]
            self.camera_pivot.rotation_x = max(-90, min(90, self.camera_pivot.rotation_x))  # Ограничение угла наклона


    def handle_keyboard_input(self):
        # Движение игрока
        if held_keys['w']:
            self.position += self.forward * PLAYER_SPEED * time.dt
        if held_keys['s']:
            self.position += self.back * PLAYER_SPEED * time.dt
        if held_keys['a']:
            self.position += self.left * PLAYER_SPEED * time.dt
        if held_keys['d']:
            self.position += self.right * PLAYER_SPEED * time.dt

    def take_damage(self, damage):
        if not self.is_blocking:
            self.health -= damage
            print(f"Игрок получил урон! Здоровье: {self.health}")
            if self.health <= 0:
                self.die()

    def die(self):
        print("Игрок побежден!")
        from ursina import application
        application.quit()
