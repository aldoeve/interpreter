#include <iostream>
#include <string>

enum class State {
    IMAGE    = 0,
    NO_IMAGE = 1,
    FAIL     = 2, 
};

inline void help() noexcept {
    const std::string_view usage{
        "\nUsage:\t./stamper.out [Option...]\n\n"
    };
    const std::string_view noImageOption{
        "\t-n\t\tOutputs only the box comment.\n"
    };
    const std::string_view helpOption   {
        "\t-h or --help    Outputs usage message.\n"
    };
    std::cout << usage << noImageOption << helpOption << std::endl;
    return;
}

inline void middleGround() noexcept {
    std::cout <<
        "__   _____  _   _ ____     ____ ___  ____  _____\n"        << 
        "\\ \\ / / _ \\| | | |  _ \\   / ___/ _ \\|  _ \\| ____|\n" <<
        " \\ V / | | | | | | |_) | | |  | | | | | | |  _|\n"        <<        
        "  | || |_| | |_| |  _ <  | |__| |_| | |_| | |___\n"        << 
        "  |_| \\___/ \\___/|_| \\_\\  \\____\\___/|____/|_____|\n" <<
    std::endl;
    return;
}

int main(int argc, char* argv[]) {
    State nextStep{State::IMAGE};

    if (argc > 1)
        nextStep = (argc == 2 && static_cast<std::string>(argv[1]) == "-n") ? State::NO_IMAGE : State::FAIL;    
    
    if (nextStep != State::FAIL)
        return 0;
    else
        help();

    return 0;
}