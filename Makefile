PKG_NAME := pypi-cryptography
URL = https://files.pythonhosted.org/packages/6d/0c/5e67831007ba6cd7e52c4095f053cf45c357739b0a7c46a45ddd50049019/cryptography-38.0.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/cryptography-vendor/snapshot/cryptography-vendor-38.0.1.tar.xz ./

include ../common/Makefile.common
