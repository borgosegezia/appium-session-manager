
class SessionManager():
    def __init__(self,host=None, port=None):
        if host is None:
            host = "localhost"
        if port is None:
            port = 4723 # port as int

        self.host = host
        self.port = port

    def set_port(self, port):
        self.port = port

    def set_host(self, port):
        self.host = host

    def get_port(self):
        return self.port

    def get_host(self):
        return self.host


    from ._methods import kill_sessions_by_udid, kill_sessions, killall_sessions, is_udid_busy, get_sessions_of_udid, busy_devices, get_sessions_by_desiredcap, get_udid_by_desiredcap, get_desiredcap_by_udid
