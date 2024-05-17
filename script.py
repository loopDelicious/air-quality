from serial import Serial

port = Serial('/dev/ttyAMA0', baudrate=9600)

def parse_data(data):
    if data[0] == 0x42 and data[1] == 0x4d:
        pm1_0_CF1 = (data[4] << 8) + data[5]
        pm2_5_CF1 = (data[6] << 8) + data[7]
        pm10_CF1 = (data[8] << 8) + data[9]
        pm1_0_atm = (data[10] << 8) + data[11]
        pm2_5_atm = (data[12] << 8) + data[13]
        pm10_atm = (data[14] << 8) + data[15]
        particles_03um = (data[16] << 8) + data[17]
        particles_05um = (data[18] << 8) + data[19]
        particles_10um = (data[20] << 8) + data[21]
        particles_25um = (data[22] << 8) + data[23]
        particles_50um = (data[24] << 8) + data[25]
        particles_100um = (data[26] << 8) + data[27]
        print(f'PM1.0 (CF=1): {pm1_0_CF1} µg/m3')
        print(f'PM2.5 (CF=1): {pm2_5_CF1} µg/m3')
        print(f'PM10 (CF=1): {pm10_CF1} µg/m3')
        print(f'PM1.0 (atmospheric): {pm1_0_atm} µg/m3')
        print(f'PM2.5 (atmospheric): {pm2_5_atm} µg/m3')
        print(f'PM10 (atmospheric): {pm10_atm} µg/m3')
        print(f'Particles > 0.3µm: {particles_03um} / 0.1L')
        print(f'Particles > 0.5µm: {particles_05um} / 0.1L')
        print(f'Particles > 1.0µm: {particles_10um} / 0.1L')
        print(f'Particles > 2.5µm: {particles_25um} / 0.1L')
        print(f'Particles > 5.0µm: {particles_50um} / 0.1L')
        print(f'Particles > 10µm: {particles_100um} / 0.1L')
    else:
        print('Data does not start with the expected start bytes.')

while True:
    if port.in_waiting > 0:
        data = port.read(port.in_waiting)
        parse_data(data)