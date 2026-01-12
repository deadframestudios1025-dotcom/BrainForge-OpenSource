from OperatorInterface import OperatorInterface
from AdvancedFunctions import AdvancedFunctions
from BehaviorModes import BehaviorModes
from CommunicationsSystems import CommunicationsSystems
from BrainForgeAssistantFunctions import BrainForgeAssistantFunctions
from BrainForge import BrainForgeBoot 
from BrainForgeFrameDesignOptions import BrainForgeFrameDesignOptions
from InterpretationLayer import InterpretationLayer
from MechanicalFunctions import MechanicalFunctions
from ModeSwitchRules import ModeSwitchRules
from NavigationSystems import NavigationSystems
from OperatorAccess import OperatorAccess
from OperatorBasicGuidanceFunctions import OperatorBasicGuidanceFunctions
from Operator_Assist_Menu import Operator_Assist_Menu
from PowerManagementSystems import PowerManagementSystems
from PrimarySensorSystems import PrimarySensorySystems
from PrimeDirectives import PrimeDirectives
from RoboticsDesignTools import RoboticsdesignTools
from Safety_Protocols import Safety_Protocols
from SystemsIOO import SystemsIOO
from SystemsMaintenance import SystemsMaintenance
from VolumeOptions import VolumeOptions
crimson = OperatorInterface()

print("=== Testing Operator Interface ===")
result = crimson.execute_operator_interface_cycle(
    touch_event="screen_touched",
    pressure=None,
    volume_db=80
)

print("BrainForge:", result)