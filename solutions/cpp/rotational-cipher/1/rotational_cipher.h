#pragma once

#include <string>

namespace rotational_cipher {

std::string rotate(const std::string& plain_text, int key_shift);

}  // namespace rotational_cipher
