﻿EXEC AddDevice CLEAN101, FALSE, FALSE, ELEVATOR_SWICTH_1, DISTRIBUTOR1;
EXEC AddDevice CLEAN102, FALSE, FALSE, ELEVATOR_SWICTH_2, DISTRIBUTOR2;
EXEC AddDevice CLEAN103, FALSE, FALSE, ELEVATOR_SWICTH_3, SCREEN2;
EXEC AddDevice CLEAN104, FALSE, FALSE, ELEVATOR_SWICTH_4, DIVERTER3;
EXEC AddDevice PRESSURE106, FALSE, FALSE, SOURCE_6, CONVEYOR6;
EXEC AddDevice PRESSURE107, FALSE, FALSE, SOURCE_7, CONVEYOR7;
EXEC AddDevice PRESSURE108, FALSE, FALSE, SOURCE_8, DIVERTER8;
EXEC AddDevice CALIBRATE111, FALSE, FALSE, FLOW6, PVC;
EXEC AddDevice CALIBRATE111, FALSE, FALSE, SOURCE_11, PVC;
EXEC AddDevice CONVEYOR1, FALSE, FALSE, SOURCE_1, LINK1;
EXEC AddDevice CONVEYOR2, FALSE, FALSE, LINK1, WEIGHT2;
EXEC AddDevice WEIGHT2, FALSE, FALSE, CONVEYOR2, SEPARATOR2;
EXEC AddDevice PROCESSOR2, FALSE, FALSE, DRIVE2, SPLITTER1;
EXEC AddDevice CONVEYOR3, FALSE, FALSE, LINK2, WEIGHT3;
EXEC AddDevice WEIGHT3, FALSE, FALSE, CONVEYOR3, SEPARATOR3;
EXEC AddDevice PROCESSOR3, FALSE, FALSE, SEPARATOR3, DIVERTER7;
EXEC AddDevice CONVEYOR4, FALSE, FALSE, DISTRIBUTOR2, PRESS1;
EXEC AddDevice CONVEYOR4, FALSE, FALSE, DISTRIBUTOR1, PRESS1;
EXEC AddDevice CONVEYOR5, FALSE, FALSE, DISTRIBUTOR1, PRESS1;
EXEC AddDevice CONVEYOR5, FALSE, FALSE, DISTRIBUTOR2, PRESS1;
EXEC AddDevice CONVEYOR6, FALSE, FALSE, PRESSURE106, WEIGHT6;
EXEC AddDevice CONVEYOR6, FALSE, FALSE, DIVERTER8, WEIGHT6;
EXEC AddDevice WEIGHT6, FALSE, FALSE, CONVEYOR6, DUST6;
EXEC AddDevice DUST6, FALSE, FALSE, WEIGHT6, PROCESSOR6;
EXEC AddDevice PROCESSOR6, FALSE, FALSE, DUST6, DIVERTER1;
EXEC AddDevice CONVEYOR7, FALSE, FALSE, PRESSURE107, WEIGHT7;
EXEC AddDevice WEIGHT7, FALSE, FALSE, CONVEYOR7, DUST7;
EXEC AddDevice DUST7, FALSE, FALSE, WEIGHT7, PROCESSOR7;
EXEC AddDevice PROCESSOR7, FALSE, FALSE, DUST7, DIVERTER2;
EXEC AddDevice CONVEYOR8, FALSE, FALSE, MAIN_WEIGHTER2, WEIGHT8;
EXEC AddDevice WEIGHT8, FALSE, FALSE, CONVEYOR8, CONVEYOR9;
EXEC AddDevice CONVEYOR9, FALSE, FALSE, WEIGHT8, SEPARATOR1;
EXEC AddDevice CONVEYOR10, FALSE, FALSE, DRIVE1, WEIGHT10;
EXEC AddDevice WEIGHT10, FALSE, FALSE, CONVEYOR10, CONVEYOR11;
EXEC AddDevice CONVEYOR11, FALSE, FALSE, WEIGHT10, LINK6;
EXEC AddDevice CONVEYOR12, FALSE, FALSE, LINK8, WEIGHT12;
EXEC AddDevice WEIGHT12, FALSE, FALSE, CONVEYOR12, DEST_LOAD;
EXEC AddDevice CONVEYOR14, FALSE, FALSE, DIVERTER8, WEIGHT14;
EXEC AddDevice WEIGHT14, FALSE, FALSE, CONVEYOR14, LINK5;
EXEC AddDevice DEST1, FALSE, TRUE, DISTRIBUTOR2, NULL;
EXEC AddDevice DEST1, FALSE, TRUE, DISTRIBUTOR1, NULL;
EXEC AddDevice DEST6, FALSE, TRUE, DISTRIBUTOR2, NULL;
EXEC AddDevice DEST6, FALSE, TRUE, DISTRIBUTOR1, NULL;
EXEC AddDevice DEST11, FALSE, TRUE, PVC, NULL;
EXEC AddDevice DEST_CLEAN, FALSE, TRUE, LINK6, NULL;
EXEC AddDevice DEST4, FALSE, TRUE, TRIPPER1, NULL;
EXEC AddDevice DEST5, FALSE, TRUE, TRIPPER2, NULL;
EXEC AddDevice DEST14, FALSE, TRUE, CHUTE1, NULL;
EXEC AddDevice DEST_LOAD, FALSE, TRUE, WEIGHT12, NULL;
EXEC AddDevice DEST_WEIGH, FALSE, TRUE, SCREEN1, NULL;
EXEC AddDevice DEST_WEIGH, FALSE, TRUE, SCREEN2, NULL;
EXEC AddDevice LINK1, FALSE, FALSE, CONVEYOR1, CONVEYOR2;
EXEC AddDevice LINK2, FALSE, FALSE, SOURCE_3, CONVEYOR3;
EXEC AddDevice LINK3, FALSE, FALSE, DIVERTER7, ELEVATOR2;
EXEC AddDevice LINK3, FALSE, FALSE, DIVERTER7, ELEVATOR1;
EXEC AddDevice LINK3, FALSE, FALSE, SPLITTER1, SPLITTER1A;
EXEC AddDevice LINK3, FALSE, FALSE, SPLITTER1, SPLITTER1B;
EXEC AddDevice LINK3, FALSE, FALSE, DIVERTER3, ELEVATOR1;
EXEC AddDevice LINK3, FALSE, FALSE, SPLITTER2, SPLITTER2A;
EXEC AddDevice LINK3, FALSE, FALSE, SPLITTER2, SPLITTER2B;
EXEC AddDevice LINK3, FALSE, FALSE, SPLITTER3, SPLITTER3A;
EXEC AddDevice LINK3, FALSE, FALSE, SPLITTER3, SPLITTER3B;
EXEC AddDevice LINK4, FALSE, FALSE, SPLITTER4, SPLITTER4A;
EXEC AddDevice LINK4, FALSE, FALSE, SPLITTER4, SPLITTER4B;
EXEC AddDevice LINK4, FALSE, FALSE, SPLITTER5, SPLITTER5A;
EXEC AddDevice LINK4, FALSE, FALSE, SPLITTER5, SPLITTER3B;
EXEC AddDevice LINK5, FALSE, FALSE, WEIGHT14, CHUTE1;
EXEC AddDevice LINK6, FALSE, FALSE, CONVEYOR11, LOAD1;
EXEC AddDevice LINK6, FALSE, FALSE, CONVEYOR11, DEST_CLEAN;
EXEC AddDevice LINK7, FALSE, FALSE, LOAD1, LINK8;
EXEC AddDevice LINK8, FALSE, FALSE, LINK7, CONVEYOR12;
EXEC AddDevice DIVERTER1, FALSE, FALSE, PROCESSOR6, SPLITTER4;
EXEC AddDevice DIVERTER1, FALSE, FALSE, PROCESSOR6, SPLITTER2;
EXEC AddDevice DIVERTER2, FALSE, FALSE, PROCESSOR7, SPLITTER3;
EXEC AddDevice DIVERTER2, FALSE, FALSE, PROCESSOR7, SPLITTER5;
EXEC AddDevice DIVERTER3, FALSE, FALSE, CLEAN104, LINK3;
EXEC AddDevice DIVERTER3, FALSE, FALSE, CLEAN104, SCREEN1;
EXEC AddDevice DIVERTER6, FALSE, FALSE, FLOW5, MAIN_WEIGHTER2;
EXEC AddDevice DIVERTER7, FALSE, FALSE, PROCESSOR3, LINK3;
EXEC AddDevice DIVERTER8, FALSE, FALSE, PRESSURE108, CONVEYOR14;
EXEC AddDevice DIVERTER8, FALSE, FALSE, PRESSURE108, CONVEYOR6;
EXEC AddDevice ELEVATOR_PATH_1, FALSE, FALSE, ELEVATOR1, ELEVATOR_SWICTH_1;
EXEC AddDevice ELEVATOR_PATH_2, FALSE, FALSE, ELEVATOR2, ELEVATOR_SWICTH_2;
EXEC AddDevice ELEVATOR_PATH_3, FALSE, FALSE, ELEVATOR3, ELEVATOR_SWICTH_3;
EXEC AddDevice ELEVATOR_PATH_4, FALSE, FALSE, ELEVATOR4, ELEVATOR_SWICTH_4;
EXEC AddDevice ELEVATOR1, FALSE, FALSE, LINK3, ELEVATOR_PATH_1;
EXEC AddDevice ELEVATOR1, FALSE, FALSE, SPLITTER1B, ELEVATOR_PATH_1;
EXEC AddDevice ELEVATOR1, FALSE, FALSE, SPLITTER2A, ELEVATOR_PATH_1;
EXEC AddDevice ELEVATOR1, FALSE, FALSE, SPLITTER3A, ELEVATOR_PATH_1;
EXEC AddDevice ELEVATOR_SWICTH_1, FALSE, FALSE, ELEVATOR_PATH_1, CLEAN101;
EXEC AddDevice ELEVATOR2, FALSE, FALSE, LINK3, ELEVATOR_PATH_2;
EXEC AddDevice ELEVATOR2, FALSE, FALSE, SPLITTER1A, ELEVATOR_PATH_2;
EXEC AddDevice ELEVATOR2, FALSE, FALSE, SPLITTER2B, ELEVATOR_PATH_2;
EXEC AddDevice ELEVATOR2, FALSE, FALSE, SPLITTER3B, ELEVATOR_PATH_2;
EXEC AddDevice ELEVATOR_SWICTH_2, FALSE, FALSE, ELEVATOR_PATH_2, CLEAN102;
EXEC AddDevice ELEVATOR3, FALSE, FALSE, SPLITTER4A, ELEVATOR_PATH_3;
EXEC AddDevice ELEVATOR3, FALSE, FALSE, SPLITTER5A, ELEVATOR_PATH_3;
EXEC AddDevice ELEVATOR_SWICTH_3, FALSE, FALSE, ELEVATOR_PATH_3, CLEAN103;
EXEC AddDevice ELEVATOR4, FALSE, FALSE, FLOW7, ELEVATOR_PATH_4;
EXEC AddDevice ELEVATOR4, FALSE, FALSE, SPLITTER4B, ELEVATOR_PATH_4;
EXEC AddDevice ELEVATOR4, FALSE, FALSE, SPLITTER3B, ELEVATOR_PATH_4;
EXEC AddDevice ELEVATOR_SWICTH_4, FALSE, FALSE, ELEVATOR_PATH_4, CLEAN104;
EXEC AddDevice FLOW5, FALSE, FALSE, MAIN_WEIGHTER1, DIVERTER6;
EXEC AddDevice FLOW6, FALSE, FALSE, MAIN_WEIGHTER2, CALIBRATE111;
EXEC AddDevice FLOW7, FALSE, FALSE, PVC, ELEVATOR4;
EXEC AddDevice PRESS1, FALSE, FALSE, CONVEYOR5, TRIPPER2;
EXEC AddDevice PRESS1, FALSE, FALSE, CONVEYOR4, TRIPPER1;
EXEC AddDevice CHUTE1, FALSE, FALSE, LINK5, DEST14;
EXEC AddDevice SEPARATOR1, FALSE, FALSE, CONVEYOR9, DRIVE1;
EXEC AddDevice SEPARATOR2, FALSE, FALSE, WEIGHT2, DRIVE2;
EXEC AddDevice SEPARATOR3, FALSE, FALSE, WEIGHT3, DRIVE3;
EXEC AddDevice DRIVE1, FALSE, FALSE, SEPARATOR1, CONVEYOR10;
EXEC AddDevice DRIVE2, FALSE, FALSE, SEPARATOR2, PROCESSOR2;
EXEC AddDevice DRIVE3, FALSE, FALSE, SEPARATOR3, PROCESSOR3;
EXEC AddDevice PVC, FALSE, FALSE, CALIBRATE111, DEST11;
EXEC AddDevice PVC, FALSE, FALSE, CALIBRATE111, FLOW7;
EXEC AddDevice DISTRIBUTOR1, FALSE, FALSE, CLEAN101, DEST6;
EXEC AddDevice DISTRIBUTOR1, FALSE, FALSE, CLEAN101, CONVEYOR5;
EXEC AddDevice DISTRIBUTOR1, FALSE, FALSE, CLEAN101, DEST1;
EXEC AddDevice DISTRIBUTOR1, FALSE, FALSE, CLEAN101, CONVEYOR4;
EXEC AddDevice DISTRIBUTOR2, FALSE, FALSE, CLEAN102, DEST6;
EXEC AddDevice DISTRIBUTOR2, FALSE, FALSE, CLEAN102, CONVEYOR5;
EXEC AddDevice DISTRIBUTOR2, FALSE, FALSE, CLEAN102, DEST1;
EXEC AddDevice DISTRIBUTOR2, FALSE, FALSE, CLEAN102, CONVEYOR4;
EXEC AddDevice SCREEN1, FALSE, FALSE, DIVERTER3, DEST_WEIGH;
EXEC AddDevice SCREEN1, FALSE, FALSE, DIVERTER3, MAIN_WEIGHTER1;
EXEC AddDevice SCREEN2, FALSE, FALSE, CLEAN103, MAIN_WEIGHTER1;
EXEC AddDevice SCREEN2, FALSE, FALSE, CLEAN103, DEST_WEIGH;
EXEC AddDevice LOAD1, FALSE, FALSE, LINK6, LINK7;
EXEC AddDevice SOURCE_11, TRUE, FALSE, NULL, CALIBRATE111;
EXEC AddDevice SOURCE_1, TRUE, FALSE, NULL, CONVEYOR1;
EXEC AddDevice SOURCE_3, TRUE, FALSE, NULL, LINK2;
EXEC AddDevice SOURCE_6, TRUE, FALSE, NULL, PRESSURE106;
EXEC AddDevice SOURCE_7, TRUE, FALSE, NULL, PRESSURE107;
EXEC AddDevice SOURCE_8, TRUE, FALSE, NULL, PRESSURE108;
EXEC AddDevice SOURCE_WEIGH, TRUE, FALSE, NULL, MAIN_WEIGHTER1;
EXEC AddDevice SPLITTER1, FALSE, FALSE, PROCESSOR2, LINK3;
EXEC AddDevice SPLITTER1A, FALSE, FALSE, LINK3, ELEVATOR2;
EXEC AddDevice SPLITTER1B, FALSE, FALSE, LINK3, ELEVATOR1;
EXEC AddDevice SPLITTER2, FALSE, FALSE, DIVERTER1, LINK3;
EXEC AddDevice SPLITTER2A, FALSE, FALSE, LINK3, ELEVATOR1;
EXEC AddDevice SPLITTER2B, FALSE, FALSE, LINK3, ELEVATOR2;
EXEC AddDevice SPLITTER3, FALSE, FALSE, DIVERTER2, LINK3;
EXEC AddDevice SPLITTER3A, FALSE, FALSE, LINK3, ELEVATOR1;
EXEC AddDevice SPLITTER3B, FALSE, FALSE, LINK3, ELEVATOR2;
EXEC AddDevice SPLITTER3B, FALSE, FALSE, LINK4, ELEVATOR4;
EXEC AddDevice SPLITTER4, FALSE, FALSE, DIVERTER1, LINK4;
EXEC AddDevice SPLITTER4A, FALSE, FALSE, LINK4, ELEVATOR3;
EXEC AddDevice SPLITTER4B, FALSE, FALSE, LINK4, ELEVATOR4;
EXEC AddDevice SPLITTER5, FALSE, FALSE, DIVERTER2, LINK4;
EXEC AddDevice SPLITTER5A, FALSE, FALSE, LINK4, ELEVATOR3;
EXEC AddDevice TRIPPER1, FALSE, FALSE, PRESS1, DEST4;
EXEC AddDevice TRIPPER2, FALSE, FALSE, PRESS1, DEST5;
EXEC AddDevice MAIN_WEIGHTER1, FALSE, FALSE, SCREEN2, FLOW5;
EXEC AddDevice MAIN_WEIGHTER1, FALSE, FALSE, SCREEN1, FLOW5;
EXEC AddDevice MAIN_WEIGHTER1, FALSE, FALSE, SOURCE_WEIGH, FLOW5;
EXEC AddDevice MAIN_WEIGHTER2, FALSE, FALSE, DIVERTER6, FLOW6;
EXEC AddDevice MAIN_WEIGHTER2, FALSE, FALSE, DIVERTER6, CONVEYOR8;
