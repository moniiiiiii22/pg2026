def bin_to_dec(binarni_cislo):
    return int(str(binarni_cislo), 2)


def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128
    assert bin_to_dec("10100111") == 167
    assert bin_to_dec(10100111) == 167


if __name__ == "__main__":
    test_bin_to_dec()
    print(bin_to_dec("10100111"))
    print(bin_to_dec(10100111))