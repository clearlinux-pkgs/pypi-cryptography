PKG_NAME := pypi-cryptography
URL = https://files.pythonhosted.org/packages/3d/5f/addb8b91fd356792d28e59a8275fec833323cb28604fb3a497c35d7cf0a3/cryptography-37.0.1.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/cryptography-vendor/snapshot/cryptography-vendor-37.0.1.tar.xz ./

include ../common/Makefile.common
