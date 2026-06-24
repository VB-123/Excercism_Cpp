#include <string>

namespace log_line {
std::string message(std::string line) {
    int i = line.find(":")+2; /* Using braces doesn't work and find returns unsigned long long, 64 bit integer and casting it to int gives an error. Also, the + 2 is to omit the : and the whitespace */
     return line.substr(i);
}

std::string log_level(std::string line) {
    int i = line.find(":");
    return line.substr(1,i-2); /* Same logic as before, skips the ] and the : in the end*/
}

std::string reformat(std::string line) {
    return log_line::message(line) +" (" + log_line::log_level(line) + ")";
}
}  // namespace log_line
