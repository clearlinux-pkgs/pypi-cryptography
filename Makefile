PKG_NAME := pypi-cryptography
URL = https://files.pythonhosted.org/packages/e3/3f/41186b1f2fd86a542d399175f6b8e43f82cd4dfa51235a0b030a042b811a/cryptography-38.0.4.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/cryptography-vendor/snapshot/cryptography-vendor-38.0.1.tar.xz ./

include ../common/Makefile.common
