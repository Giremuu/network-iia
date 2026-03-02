#include <iostream>
#include <string>

class Workstation {
private:
    std::string hostname;
    std::string ip_address;

public:
    Workstation(std::string hostname, std::string ip_address)
        : hostname(hostname), ip_address(ip_address) {}

    std::string getHostname() const {
        return hostname;
    }

    void login(const std::string& username) {
        std::cout << username << " logged into "
                  << hostname << std::endl;
    }

    void run_application(const std::string& app_name) {
        std::cout << "Running " << app_name
                  << " on " << hostname << std::endl;
    }
};


class User {
private:
    std::string username;

public:
    User(std::string username)
        : username(username) {}

    void authenticate() {
        std::cout << "User " << username
                  << " authenticated" << std::endl;
    }

    void request_access(Workstation& workstation) {
        std::cout << username
                  << " requests access to "
                  << workstation.getHostname()
                  << std::endl;

        workstation.login(username);
    }
};


int main() {
    Workstation pc("PC-01", "192.168.1.50");
    User user("alice");

    user.authenticate();
    user.request_access(pc);
    pc.run_application("Browser");

    return 0;
}