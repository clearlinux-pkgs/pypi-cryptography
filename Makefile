PKG_NAME := pypi-cryptography
URL = https://files.pythonhosted.org/packages/ef/33/87512644b788b00a250203382e40ee7040ae6fa6b4c4a31dcfeeaa26043b/cryptography-41.0.4.tar.gz
ARCHIVES = $(CGIT_BASE_URL)/projects/cryptography-vendor/snapshot/cryptography-vendor-41.0.4.tar.xz ./

include ../common/Makefile.common
