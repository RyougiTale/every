#include <vector>
#include <string>

class Client
{

    void register_to(EveryServer &server)
    {
    }
};

class EveryServer
{
public:
    EveryServer(std::string ip)
    {
    }
    void connect_server(EveryServer &server)
    {
    }

private:
    std::vector<std::string> servers;
    std::vector<Client> clients;
};

int main()
{
    return 0;
}