#include <iostream>
#include <string>
#include <vector>
#include <ctime>

enum class State {
    IMAGE    = 0,
    NO_IMAGE = 1,
    FAIL     = 2, 
};
//-----------------------------------------------------------------------------------
//Shows appropriate usage of the program.
inline void help() noexcept {
    std::string_view usage{
        "\nUsage:\t./stamper.out [Option...] <CommentStr>\n\n"
    };
    std::string_view noImageOption{
        "\t-n\t\tOutputs only the box comment.\n"
    };
    std::string_view helpOption   {
        "\t-h or --help    Outputs usage message.\n"
    };
    std::cout << usage << noImageOption << helpOption << std::endl;
    return;
}

/*

    developer:
    Date:                           
    Project Name:
    Desc:

*/



//Prints a simple box comment. The name is hard coded, but
//it can be changed for anyone else.
inline void boxComment(std::string_view comment) noexcept{
    const int width {84};
    const std::time_t now         {std::time(0)};
    std::string_view  horizontal  {"-"};
    std::string_view  vertical    {"|"};
    std::string_view  name        {"Aldo Vera-Espinoza"};
    std::string       projectName {};
    std::string       desc        {};
    std::vector<const char*> initals {
        "    ___     _______ ",
        "   / \\ \\   / / ____|",
        "  / _ \\ \\ / /|  _|  ",
        " / ___ \\ V / | |___ ",
        "/_/   \\_\\_/  |_____|",
    };

    std::cout << "Input project name: ";
    std::cin >> projectName;
    std::cout << "\nInput project description: ";
    std::cin >> desc;
    std::cout << std::endl;

    auto horizontalSides = [comment, horizontal]{
        std::cout << comment;
        for(short int i{0}; i < width; ++i)
            std::cout << horizontal;
        std::cout << comment << std::endl;
    };

    horizontalSides();
    
    std::cout << comment << '\t' << "Developer: " << name << std::endl;
    std::cout << comment << '\t' << "Date: " << ctime(&now) << std::endl;
    std::cout << comment << '\n' << std::endl;
    std::cout << comment << '\t' << "Project Name: " << projectName << std::endl;
    std::cout << comment << '\t' << "Description: " << std::endl;

    horizontalSides();

    return;
}

//Prints an image of smug Pekora.
inline void image(std::string_view comment) noexcept {
    //Hard coded because I do not want another file to keep track of.
    std::vector<const char*> image {
        "⠀⠀⠀⠀⠀⡆⠀⠀⠀⢲⠀⠀⠹⡄⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⡞⠀⠐⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⢣⡀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⢸⡓⠛⠳⠺⣇⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⢀⣷⣄⡀⠘⢦⣀⣠⡴⠶⠚⠛⠛⠃⠒⠒⠒⠚⠦⢀⣻⡉⠉⠉⠑⠒⠢⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⣶⢒⢲⡄⠀⠙⠺⣯⣡⢤⡚⠋⠉⠉⠐⠒⠉⠉⠓⠒⠢⠄⣀⠀⠀⠀⠀⠈⠑⠦⡀⠀⠀⠀⠀⠀⠉⠒⢤⡀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠈⠣⣀⡷⠀⣠⣾⠟⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠂⢀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠈⠑⢄⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠁⢠⣾⠏⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⢄⠀⠀⠀⠑⢆⠀⠀⠀⠀⠀⠀⠀⠙⢄⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⡰⡷⠁⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⠈⠳⡀⠀⠀",
        "⠀⠀⠀⢀⣼⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠑⡄⠀",
        "⠀⠀⢀⣞⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠘⣄",
        "⠀⠀⡜⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢆⠀⠀⢳⡀⠀⠀⠀⠀⠀⠀⠠⡸",
        "⠀⣰⠱⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⠀⠈⣷⠀⠀⠀⠀⠀⠀⠀⠘",
        "⢠⠇⡆⠀⠀⠀⢠⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠀⠀⠀⢹⡀⠀⢹⡆⠀⠀⠀⠀⠀⢄⠀",
        "⡼⢰⠀⠀⠀⠀⡞⠀⠀⠀⠀⠀⠀⣿⡀⡄⠀⠀⠀⢠⣀⠀⡏⢣⡀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠸⡄⠀⠀⠀⠀⣇⠀⠀⣷⠀⠀⠀⠀⠀⠀⠙",
        "⠣⡇⠀⠀⠀⢠⡇⠀⠀⠀⢰⠂⠀⡏⣇⣷⠀⠀⠀⠈⢯⠉⢻⠒⠳⡄⠀⠀⠀⠀⢳⠀⠀⠀⠀⣇⠀⠀⠀⠀⢸⠀⠀⢻⡄⠀⠀⠀⠀⠀⠀",
        "⠀⠃⠀⠀⠀⢸⠇⠀⠀⠀⢸⠀⢸⡧⢏⢹⡀⠀⠀⠀⠀⠑⠺⡇⠊⠘⢢⠀⠀⠀⠈⣧⡀⠀⠀⢸⠀⠀⠀⠀⢸⡅⠀⢸⡇⠀⠀⠀⠀⠀⠀",
        "⠠⠀⠀⠀⠀⢸⠇⠀⠀⠀⣾⠀⡿⠄⢼⠾⢧⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠑⢤⡀⠀⠸⡳⡀⠀⢸⠀⠀⠀⠀⢸⡄⠀⠈⣷⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⡀⠀⠸⡇⠀⠀⢀⡗⣰⠁⠀⠀⢣⡌⢢⡀⠀⠀⠀⠀⡇⠀⣰⣂⣀⣀⣭⣶⣤⣷⣿⣄⠘⡆⠀⠀⠀⢸⠆⠀⠀⣿⣤⣤⣤⢶⠾⠷",
        "⠀⠀⠰⣧⠀⠀⣇⠀⠀⣼⣷⠃⠀⠀⣀⣠⣿⡀⠑⢄⡀⠀⠀⡇⠀⠙⠿⣿⣿⡿⣿⣿⣿⡆⠈⢲⡇⠀⠀⠀⣼⠀⠀⠀⣿⣧⣐⣤⣮⣼⣷",
        "⢸⠀⠀⣿⡀⠀⢿⠀⣰⣿⣧⣶⣶⣿⣿⣯⠀⠁⠀⠀⠈⠢⢄⡇⠀⠀⢰⡾⠟⠷⠟⠛⣻⠃⠀⢰⠃⠀⠀⣰⡇⠀⠀⠀⣏⣿⡿⢟⢻⣿⣋",
        "⢸⡆⠀⢿⣧⠀⢸⣦⠟⠛⠛⣿⣏⣻⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠒⠒⠒⠋⠁⠀⠀⡸⠀⢀⣴⡟⠀⠀⠀⠀⣿⡟⣡⡼⠋⣠⠟",
        "⠨⣇⠀⠘⣿⣦⠀⢿⡀⠀⠺⣟⣉⣉⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⢰⡅⠔⠋⣿⠀⠀⠀⠀⠀⣿⡼⠋⠀⢸⣁⠀",
        "⡇⢹⡀⠀⢻⣿⣧⡈⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠛⠛⢦⠀⠀⠀⠀⠀⠀⠀⣟⠀⠀⠀⠀⠀⡿⠛⠢⣄⠀⠉⣿",
        "⣷⠀⢧⠀⠘⣿⡸⢿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠴⡪⠃⠀⠀⠈⡇⠀⠀⠀⠀⢀⣴⣯⠀⠀⠀⠀⣸⡇⠀⠀⠈⢣⢸⠇",
        "⣿⡄⠈⣧⡀⢸⡇⣹⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠠⡦⠴⠖⠮⠭⠒⠉⠀⠀⠀⢀⡼⠁⠀⠀⣠⣴⣿⡛⡧⠀⠀⠀⠀⣿⠃⠀⠀⠀⠀⠼⣇", 
        "⠙⢳⡀⢸⡙⠲⢷⣸⣿⡷⠦⣀⡀⠀⠀⠀⠀⠀⠀⠳⢄⡀⠀⠀⠀⣀⣀⡠⠔⠋⣀⣠⡴⠛⠉⠀⠀⠉⡧⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠠⡟",
        "⠀⠀⠁⠘⣇⠀⠀⠙⣿⡅⢠⡟⠉⠙⠓⠒⠦⠤⠤⠤⣤⡬⣭⣭⣭⠬⠴⡒⢚⡿⠛⠉⠀⠀⠀⠀⠀⠀⡗⠀⠀⠀⢸⡏⠀⠀⠀⠀⠀⠀⠘",
    };

    for(const auto & i: image){
        std::cout << comment << i << std::endl;
    }

    return;
}

int main(int argc, char* argv[]) {
    State nextStep {State::IMAGE};
    std::string comment {"#"};

    //Resolves what flags or input was given to the program.
    if (argc > 3) nextStep = State::FAIL;

    for(int i {1}; nextStep != State::FAIL && i < argc; ++i){
        std::string_view cmdOption {static_cast<std::string_view>(argv[i])};
        if (cmdOption.compare("-n") == 0)
            nextStep = State::NO_IMAGE;
        else
            comment = cmdOption;
    }

    //Decides how to format the output.
    if(nextStep != State::FAIL){
        boxComment(comment);
        std::cout << "\n\n" << std::endl;
        if (nextStep == State::IMAGE) {
            image(comment);
            std::cout << std::endl;
        }
    }
    else
        help();

    return 0;
}