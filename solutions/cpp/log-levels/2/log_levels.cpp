#include <string>

namespace log_line {
std::string message(const std::string& line) {
    /*Iteration 2: Used auto for auto type deduction. Works perfectly, as the return type of std::string::find() is std::size_t and the type of the parameters for std::string::substr() is the same too.*/
    auto msg_idx{line.find(":")+2}; /* The + 2 is to omit the : and the whitespace */
     return line.substr(msg_idx);
}

std::string log_level(const std::string& line) {
    /*Iteration 2: Better variable names and auto type deduction.*/
    auto level_end{line.find(":") - 2}; /* The - 2 skips the ] and the : in the end*/
    return line.substr(1,level_end); 
}

std::string reformat(const std::string& line) {
    /*Iteration 2: Removed the "log_line::". Also, used pass by reference, instead of pass by value.*/
    return message(line) +" (" + log_level(line) + ")";
}
}  // namespace log_line
