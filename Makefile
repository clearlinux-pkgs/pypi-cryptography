PKG_NAME := pypi-cryptography
URL = https://files.pythonhosted.org/packages/10/a7/51953e73828deef2b58ba1604de9167843ee9cd4185d8aaffcb45dd1932d/cryptography-36.0.2.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/cryptography-vendor/snapshot/cryptography-vendor-36.0.1.tar.xz ./

include ../common/Makefile.common
