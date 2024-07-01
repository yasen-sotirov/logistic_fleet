from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine
from screens.welcome_screen import welcome_screen


app_data = ApplicationData()
cmd_factory = CommandFactory(app_data)
engine = Engine(cmd_factory)
print(welcome_screen)


engine.start()



'''

CreateDeliveryPackage MELBOURNE AliCE_SPRinGS 1000 Ivan Ivanov ivan@abv.bg 0888111222
CreateDeliveryPackage BrisBANE DARwIN 1000 Ivan Ivanov ivan@abv.bg 0888111222
CreateDeliveryPackage peRTH AliCE_SPRinGS 1000 Ivan Ivanov ivan@abv.bg 0888111222
CreateDeliveryPackage DARwIN peRTH 1000 Ivan Ivanov ivan@abv.bg 0888111222
CreateDeliveryPackage AliCE_SPRinGS DARwIN 8000 Ivan Ivanov ivan@abv.bg 0888111222
CreateDeliveryPackage ADElaIDE sydNey 8000 Ivan Ivanov ivan@abv.bg 0888111222
ViewPackages sydNey
ViewUnassignedPackages
CreateDeliveryRoute 20/08/2023 17:30 mELBOURNe AliCE_SPRinGS
CreateDeliveryRoute 20/08/2023 17:30 BrisBANE DARwIN
CreateDeliveryRoute 20/08/2023 17:30 peRTH AliCE_SPRinGS
CreateDeliveryRoute 20/08/2023 17:30 DARwIN peRTH
CreateDeliveryRoute 20/08/2023 17:30 AliCE_SPRinGS DARwIN
CreateDeliveryRoute 20/08/2023 17:30 ADElaIDE sydNey
EnrollTruckToLocation Actors mELBOURNe
EnrollTruckToLocation man BrisBANE
EnrollTruckToLocation Scania peRTH
EnrollTruckToLocation Actors DARwIN
EnrollTruckToLocation Scania AliCE_SPRinGS
EnrollTruckToLocation man ADElaIDE
SearchRoute sydNey
ViewCustomerByPhoneNumber 0888111222 2001
ViewCustomerByPhoneNumber 0888111222 2002
ViewCustomerByPhoneNumber 0888111222 2003
ViewCustomerByPhoneNumber 0888111222 2004
ViewCustomerByPhoneNumber 0888111222 2005
ViewCustomerByPhoneNumber 0888111222 2006
AssignTruckToDeliveryRoute mELBOURNe 3001
AssignTruckToDeliveryRoute BrisBANE 3002
AssignTruckToDeliveryRoute peRTH 3003
AssignTruckToDeliveryRoute DARwIN 3004
AssignTruckToDeliveryRoute AliCE_SPRinGS 3005
AssignTruckToDeliveryRoute ADElaIDE 3006
LoadPackagesToTruck 1026 3001
LoadPackagesToTruck 1011 3002
LoadPackagesToTruck 1001 3003
LoadPackagesToTruck 1027 3004
LoadPackagesToTruck 1002 3005
LoadPackagesToTruck 1012 3006
ViewUnassignedPackages
ViewCustomerByPhoneNumber 0888111222 2001
ViewCustomerByPhoneNumber 0888111222 2002
ViewCustomerByPhoneNumber 0888111222 2003
ViewCustomerByPhoneNumber 0888111222 2004
ViewCustomerByPhoneNumber 0888111222 2005
ViewCustomerByPhoneNumber 0888111222 2006
ViewRoutes
SetCurrentDateTime 21/08/2023 06:00
ViewRoutes
ViewCustomerByPhoneNumber 0888111222 2001
SetCurrentDateTime 25/08/2023 06:40
ViewRoutes
ViewCustomerByPhoneNumber 0888111222 2001
ViewCustomerByPhoneNumber 0888111222 2002
ViewCustomerByPhoneNumber 0888111222 2003
ViewCustomerByPhoneNumber 0888111222 2004
ViewCustomerByPhoneNumber 0888111222 2005
ViewCustomerByPhoneNumber 0888111222 2006
ViewTrucksAtLocation MELBOURNE
ViewTrucksAtLocation BRISBANE
ViewTrucksAtLocation sydNey
ViewTrucksAtLocation adELAIDe
ViewTrucksAtLocation ALICE_SPRINGS
ViewTrucksAtLocation DARwIN
ViewTrucksAtLocation peRTH
ViewPackages sydNey
ViewPackages mElBOURNe
ViewPackages BRISBANE
ViewPackages adELAIDe
ViewPackages ALICE_SPRINGS
ViewPackages DARwIN
ViewPackages peRTH
ViewAllTrucks
end

'''

