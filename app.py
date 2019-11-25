import json
import random
from time import sleep
import paho.mqtt.client as mqtt

# 使用docker运行时，需要是外网的地址

THINGSBOARD_HOST = '172.17.130.117'
ACCESS_TOKEN = '6F54a9PFnXBulm5sjMny'

def on_connect(client, userdata, flags, rc):
  print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
  print(msg.topic+" "+str(msg.payload))

#创建MQTT连接
client = mqtt.Client()
#设置用户名
client.username_pw_set(ACCESS_TOKEN)

#两个事件
client.on_connect = on_connect
client.on_message = on_message

#开始连接
client.connect(THINGSBOARD_HOST, 1883, 60)
#开始处理
client.loop_start()

data = {}

#循环生成数据
while True:
    # 熔炉温度
    newnumber = "%.2f" % random.random()
    data['StoveTemperature'] = random.randint(420, 430) + float(newnumber)

    # 炉咀温度
    newnumber = "%.2f" % random.random()
    data['StoveMouthTemperature'] = random.randint(420, 430) + float(newnumber)

    # 模具入水温度
    newnumber = "%.2f" % random.random()
    data['MouldInputWaterTemperature'] = random.randint(30, 80) + float(newnumber)

    # 模具出水温度
    newnumber = "%.2f" % random.random()
    data['MouldOutputWaterTemperature'] = random.randint(40, 100) + float(newnumber)

    # 机器油压力
    newnumber = "%.2f" % random.random()
    data['MachineOilPressure'] = random.randint(400, 500) + float(newnumber)

    # 机器空气压力
    newnumber = "%.2f" % random.random()
    data['MachineAirPressure'] = random.randint(400, 500) + float(newnumber)

    # 电流
    newnumber = "%.2f" % random.random()
    data['GalvanicCurrent'] = random.randint(18, 20) + float(newnumber)

    # 电压
    newnumber = "%.2f" % random.random()
    data['Voltage'] = random.randint(240, 450) + float(newnumber)

    # client.publish("v1/devices/me/telemetry",str(json.dumps(data)),2)
    client.publish("v1/devices/me/telemetry", json.dumps(data), 2)
    print(str(json.dumps(data)))

    sleep(5)
