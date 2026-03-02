class Workstation:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        self.ip_address = ip_address

    def login(self, username):
        print(f"{username} logged into {self.hostname}")

    def run_application(self, app_name):
        print(f"Running {app_name} on {self.hostname}")


class User:
    def __init__(self, username):
        self.username = username

    def authenticate(self):
        print(f"User {self.username} authenticated")

    def request_access(self, workstation: Workstation):
        print(f"{self.username} requests access to {workstation.hostname}")
        workstation.login(self.username)


# Example usage
if __name__ == "__main__":
    pc = Workstation("PC-01", "192.168.1.50")
    user = User("alice")

    user.authenticate()
    user.request_access(pc)
    pc.run_application("Browser")