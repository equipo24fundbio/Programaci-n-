EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Display_Character:RC1602A U1
U 1 1 61869945
P 8100 3350
F 0 "U1" H 8100 4231 50  0000 C CNN
F 1 "Display 16x2" H 8100 4140 50  0000 C CNN
F 2 "Display:RC1602A" H 8200 2550 50  0001 C CNN
F 3 "http://www.raystar-optronics.com/down.php?ProID=18" H 8200 3250 50  0001 C CNN
	1    8100 3350
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR0101
U 1 1 618930B1
P 5750 4800
F 0 "#PWR0101" H 5750 4550 50  0001 C CNN
F 1 "Earth" H 5750 4650 50  0001 C CNN
F 2 "" H 5750 4800 50  0001 C CNN
F 3 "~" H 5750 4800 50  0001 C CNN
	1    5750 4800
	1    0    0    -1  
$EndComp
Wire Wire Line
	5250 1500 5950 1500
Wire Wire Line
	5950 1500 5950 1950
$Comp
L power:Earth #PWR0102
U 1 1 6189D391
P 5600 1300
F 0 "#PWR0102" H 5600 1050 50  0001 C CNN
F 1 "Earth" H 5600 1150 50  0001 C CNN
F 2 "" H 5600 1300 50  0001 C CNN
F 3 "~" H 5600 1300 50  0001 C CNN
	1    5600 1300
	1    0    0    -1  
$EndComp
Wire Wire Line
	5250 1400 5250 1150
Wire Wire Line
	5250 1150 5600 1150
Wire Wire Line
	5600 1150 5600 1300
$Comp
L power:Earth #PWR0104
U 1 1 618B9A0C
P 8100 4150
F 0 "#PWR0104" H 8100 3900 50  0001 C CNN
F 1 "Earth" H 8100 4000 50  0001 C CNN
F 2 "" H 8100 4150 50  0001 C CNN
F 3 "~" H 8100 4150 50  0001 C CNN
	1    8100 4150
	1    0    0    -1  
$EndComp
Wire Wire Line
	8100 4150 8100 4050
Connection ~ 5950 1500
Wire Wire Line
	5150 2750 5350 2750
Wire Wire Line
	6950 3750 7300 3750
Wire Wire Line
	7300 3750 7300 3850
Wire Wire Line
	7300 3850 7700 3850
Wire Wire Line
	6950 3050 7350 3050
Wire Wire Line
	7350 3050 7350 3750
Wire Wire Line
	7350 3750 7700 3750
Wire Wire Line
	7700 3650 7400 3650
Wire Wire Line
	7400 3650 7400 3150
Wire Wire Line
	7400 3150 6950 3150
Wire Wire Line
	7700 3550 7450 3550
Wire Wire Line
	7450 3550 7450 4050
Wire Wire Line
	7450 4050 6950 4050
Wire Wire Line
	5350 3050 5100 3050
Wire Wire Line
	5100 3050 5100 5100
Wire Wire Line
	5100 5100 7500 5100
Wire Wire Line
	7500 5100 7500 3050
Wire Wire Line
	7500 3050 7700 3050
Wire Wire Line
	7700 2850 7150 2850
Wire Wire Line
	7150 2850 7150 5000
Wire Wire Line
	7150 5000 5150 5000
Wire Wire Line
	5150 5000 5150 3850
Wire Wire Line
	5150 3850 5350 3850
Wire Wire Line
	8100 2250 8600 2250
Wire Wire Line
	8600 2250 8600 3150
Wire Wire Line
	8600 3150 8500 3150
Wire Wire Line
	8100 2250 8100 2650
Text Label 5300 1500 0    50   ~ 0
Alimentación
Text Label 8100 2650 0    50   ~ 0
Alimentación
Text Label 8600 3150 0    50   ~ 0
Alimentación
$Comp
L Device:Battery_Cell BT1
U 1 1 618709C8
P 3050 1950
F 0 "BT1" H 3168 2046 50  0000 L CNN
F 1 "Battery" H 3168 1955 50  0000 L CNN
F 2 "" V 3050 2010 50  0001 C CNN
F 3 "~" V 3050 2010 50  0001 C CNN
	1    3050 1950
	1    0    0    -1  
$EndComp
Wire Wire Line
	3050 1400 3650 1400
Wire Wire Line
	3050 1750 3050 1400
Connection ~ 8100 2250
Wire Wire Line
	5950 1500 8100 1500
Wire Wire Line
	8100 1500 8100 2250
Text Label 7600 3850 0    50   ~ 0
P7
Text Label 7600 3750 0    50   ~ 0
P6
Text Label 7600 3650 0    50   ~ 0
P5
Text Label 7600 3550 0    50   ~ 0
P4
Text Label 7600 3050 0    50   ~ 0
E
Text Label 7600 2850 0    50   ~ 0
4
Wire Wire Line
	5750 4550 5750 4800
$Comp
L Connector:Raspberry_Pi_2_3 J1
U 1 1 618B0D1C
P 6150 3250
F 0 "J1" H 6150 4731 50  0000 C CNN
F 1 "Raspberry_Pi_2_3" H 6150 4640 50  0000 C CNN
F 2 "" H 6150 3250 50  0001 C CNN
F 3 "https://www.raspberrypi.org/documentation/hardware/raspberrypi/schematics/rpi_SCH_3bplus_1p0_reduced.pdf" H 6150 3250 50  0001 C CNN
	1    6150 3250
	1    0    0    -1  
$EndComp
$Comp
L power:Earth #PWR?
U 1 1 618BD605
P 3050 2050
F 0 "#PWR?" H 3050 1800 50  0001 C CNN
F 1 "Earth" H 3050 1900 50  0001 C CNN
F 2 "" H 3050 2050 50  0001 C CNN
F 3 "~" H 3050 2050 50  0001 C CNN
	1    3050 2050
	1    0    0    -1  
$EndComp
Wire Wire Line
	3750 2950 3750 3100
Wire Wire Line
	3800 2950 3750 2950
$Comp
L power:Earth #PWR0103
U 1 1 618AC586
P 3750 3100
F 0 "#PWR0103" H 3750 2850 50  0001 C CNN
F 1 "Earth" H 3750 2950 50  0001 C CNN
F 2 "" H 3750 3100 50  0001 C CNN
F 3 "~" H 3750 3100 50  0001 C CNN
	1    3750 3100
	1    0    0    -1  
$EndComp
Wire Wire Line
	3700 2850 3800 2850
$Comp
L Device:Microphone_Condenser MK1
U 1 1 618A7FA0
P 3500 2850
F 0 "MK1" V 3767 2850 50  0000 C CNN
F 1 "Condensador " V 3676 2850 50  0000 C CNN
F 2 "" V 3500 2950 50  0001 C CNN
F 3 "~" V 3500 2950 50  0001 C CNN
	1    3500 2850
	0    -1   -1   0   
$EndComp
$Comp
L Device:Speaker LS1
U 1 1 618A6AB4
P 4000 2850
F 0 "LS1" H 4170 2846 50  0000 L CNN
F 1 "Speaker" H 4170 2755 50  0000 L CNN
F 2 "" H 4000 2650 50  0001 C CNN
F 3 "~" H 3990 2800 50  0001 C CNN
	1    4000 2850
	1    0    0    -1  
$EndComp
Wire Wire Line
	2700 2750 2450 2750
Wire Wire Line
	2450 2750 2450 2400
Wire Wire Line
	2450 2400 5050 2400
Wire Wire Line
	5050 2400 5050 2650
Wire Wire Line
	5050 2650 5350 2650
Wire Wire Line
	2400 2950 2700 2950
$Comp
L Amplifier_Operational:LM4562 U2
U 1 1 618777A2
P 3000 2850
F 0 "U2" H 3000 3217 50  0000 C CNN
F 1 "Amplificador" H 3000 3126 50  0000 C CNN
F 2 "" H 3000 2850 50  0001 C CNN
F 3 "http://www.ti.com/lit/ds/symlink/lm4562.pdf" H 3000 2850 50  0001 C CNN
	1    3000 2850
	1    0    0    -1  
$EndComp
Connection ~ 2400 3000
Wire Wire Line
	2400 2950 2400 3000
Wire Wire Line
	2400 3050 2400 3000
$Comp
L power:Earth #PWR0108
U 1 1 618739D1
P 2400 3000
F 0 "#PWR0108" H 2400 2750 50  0001 C CNN
F 1 "Earth" H 2400 2850 50  0001 C CNN
F 2 "" H 2400 3000 50  0001 C CNN
F 3 "~" H 2400 3000 50  0001 C CNN
	1    2400 3000
	1    0    0    -1  
$EndComp
$Comp
L Interruptor:MS12ASG40 SW1
U 1 1 6186454B
P 3650 1400
F 0 "SW1" H 4450 1787 60  0000 C CNN
F 1 "Switch Slide" H 4450 1681 60  0000 C CNN
F 2 "MS12ASG40_NKK" H 4450 1640 60  0001 C CNN
F 3 "" H 3650 1400 60  0000 C CNN
	1    3650 1400
	1    0    0    -1  
$EndComp
$EndSCHEMATC
