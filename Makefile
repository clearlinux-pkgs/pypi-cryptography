PKG_NAME := pypi-cryptography
URL = https://files.pythonhosted.org/packages/16/a7/38fdcdd634515f589c8c723608c0f0b38d66c6c2320b3095967486f3045a/cryptography-41.0.5.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/cryptography-vendor/snapshot/cryptography-vendor-41.0.4.tar.xz ./

include ../common/Makefile.common
