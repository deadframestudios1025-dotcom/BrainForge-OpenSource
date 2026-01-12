class OperatorBasicGuidanceFunctions:
    def __init__(self):
        self.OperatorBasicGuidanceFunctions = [
            "Operator Basic Guidance Functions",
            "Move = Function",
            "Stop = Function",
            "TurnLeft = Function",
            "TurnRight = Function",
            "TurnAround = Function",
            "Lower = Function",
            "Rise = Function",
            "KneelDown = Function",
            "BendDown = Function",
            "PickUp = Function",
            "Lift = Function",
            "PutDown = Function",
            "Throw = Function",
            "LookUp = Function",
            "LookForward = Function",
            "LookDown = Function",
            "LookLeft = Function",
            "LookRight = Function",
            "LookAround = Function"
        ]
        self.Operator_Advanced_Guidance = [
            "OAG = OperatorAdvancedGuidance",
            "ODHE = Operator Direct Head and Eye Sync",
            "OCHUD = Operator Cockpit Heads_Up_Display",
            "OARHUD = Operator Augmented Reality Heads_Up_Display"
        ]
    def move(self, direction=None):
        pass
    def stop(self):
        pass
    def turn(self, direction=None):
        pass
    def change_height(self, action=None):
        pass
    def manipulate_object(self, action=None):
        pass
    def adjust_view(self, direction=None):
        pass
    def sync_head_eye(self, operator_state=None):
        pass
    def update_cockpit_hud(self, hud_data=None):
        pass
    def update_ar_hud(self, ar_data=None):
        pass
    def execute_operator_guidance_cycle(
        self,
        direction=None,
        height_action=None,
        object_action=None,
        view_direction=None,
        operator_state=None,
        hud_data=None,
        ar_data=None
    ):
        basic_move = self.move(direction)
        basic_stop = self.stop()
        basic_turn = self.turn(direction)
        basic_height = self.change_height(height_action)
        basic_object = self.manipulate_object(object_action)
        basic_view = self.adjust_view(view_direction)
        adv_sync = self.sync_head_eye(operator_state)
        adv_hud = self.update_cockpit_hud(hud_data)
        adv_ar = self.update_ar_hud(ar_data)
        return (

            basic_move,
            basic_stop,
            basic_turn,
            basic_height,
            basic_object,
            basic_view,
            adv_sync,
            adv_hud,
            adv_ar
        )
