import requests
class Esp:
    def __init__(self, esp_ip) -> None:
        self.esp_ip = esp_ip
    
    def change_led_state(self, state):
        if state in ('on','off'):
            print(requests.request("GET",'http://'+self.esp_ip+f'/0/{state}'))
        else:
            raise Exception("State can be set to either 'on' or 'off'")

    def change_relay_state(self, state):
        if state in ('on','off'):
            print(requests.request("GET",'http://'+self.esp_ip+f'/1/{state}'))
        else:
            raise Exception("State can be set to either 'on' or 'off'")
