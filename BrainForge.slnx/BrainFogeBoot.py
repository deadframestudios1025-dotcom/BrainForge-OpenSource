# BrainForge Boot Logic
# Initializes core systems and prepares organ modules

class BrainForgeBoot:
    def __init__(self):
        self.systems_initialized = False
        self.organs = {}

    def register_organ(self, name, organ_instance):
        self.organs[name] = organ_instance

    def initialize_systems(self):
        print("[BrainForge] Initializing core systems...")

        # Initialize all registered organs
        for name, organ in self.organs.items():
            if hasattr(organ, "activate"):
                organ.activate()
            print(f"[BrainForge] Organ loaded: {name}")

        self.systems_initialized = True
        print("[BrainForge] Core systems initialized.")
        return True
