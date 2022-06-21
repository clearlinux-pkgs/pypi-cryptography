PKG_NAME := pypi-cryptography
URL = https://files.pythonhosted.org/packages/67/82/9dd8ef695c7f928b25927e8956f73bdba09a752a51871678f320c498c535/cryptography-37.0.3.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/cryptography-vendor/snapshot/cryptography-vendor-37.0.2.tar.xz ./

include ../common/Makefile.common
