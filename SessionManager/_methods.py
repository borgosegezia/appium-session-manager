import json, requests

def kill_sessions_by_udid(self, udid):
    session_list = self.get_sessions_of_udid(udid=udid)
    self.kill_sessions(session_list=session_list)


def kill_sessions(self, session_list):
    for session in session_list:
        status_codes.append(requests.delete("http://" + self.host + ":" + str(self.port) + "/session/" + session).status_code)


def killall_sessions(self):
    resp = requests.get("http://" + self.host + ":" + str(self.port) + "/sessions/")
    json_data = json.loads(resp.text)

    for n in range(len(json_data["value"])):
        status_codes.append(requests.delete("http://" + self.host + ":" + str(self.port) + "/session/" + json_data["value"][n]["id"]).status_code)

def is_udid_busy(self, udid):
    device_list = self.busy_devices()
    return udid in device_list


def get_sessions_of_udid(self, udid):
    resp = requests.get("http://" + self.host + ":" + str(self.port) + "/sessions/")
    json_data = json.loads(resp.text)
    session_list = []

    for n in range(len(json_data["value"])):
        if json_data["value"][n]["capabilities"]["deviceUDID"] == udid:
            session_list.append(json_data["value"][n]["id"])

    return session_list


def busy_devices(self):
    resp = requests.get('http://' + self.host + ':' + str(self.port) + '/sessions/')
    json_data = json.loads(resp.text)
    device_list = []

    for n in range(len(json_data["value"])):
        device_list.append(json_data["value"][n]["capabilities"]["deviceUDID"])

    return device_list


def get_sessions_by_desiredcap(self, desiredcap="platformName", matching="Android"):
    resp = requests.get("http://" + self.host + ":" + str(self.port) + "/sessions/")
    json_data = json.loads(resp.text)
    session_list = []

    for n in range(len(json_data["value"])):
        try:
            if json_data["value"][n]["capabilities"]["desired"][desiredcap] == matching:
                session_list.append(json_data["value"][n]["id"])
        except KeyError: # Desired Capability not setted
            pass

    return session_list


def get_udid_by_desiredcap(self, desiredcap="platformName", matching="Android"):
    resp = requests.get("http://" + self.host + ":" + str(self.port) + "/sessions/")
    json_data = json.loads(resp.text)
    udid_list = []

    for n in range(len(json_data["value"])):
        try:
            if json_data["value"][n]["capabilities"]["desired"][desiredcap] == matching:
                udid_list.append(json_data["value"][n]["capabilities"]["deviceUDID"])
        except KeyError: # Desired Capability not setted
            pass

    return udid_list

def get_desiredcap_by_udid(self, udid, desiredcap="platformName"):
    resp = requests.get("http://" + self.host + ":" + str(self.port) + "/sessions/")
    json_data = json.loads(resp.text)
    desiredcaps = []

    for n in range(len(json_data["value"])):
        if json_data["value"][n]["capabilities"]["deviceUDID"] == udid:
            try:
                desiredcaps.append(json_data["value"][n]["capabilities"][desiredcap])
            except KeyError:
                pass

    return desiredcaps
