INSTALL=${HOME}/PythonLib/lib

CATPDF=${INSTALL}/CatpdfTool
EXEC=${CATPDF}/catpdf

.PHONY: install uninstall mkbash

install : 
	mkdir ${CATPDF}
	mkdir ${CATPDF}/latex
	mkdir ${CATPDF}/work
	cp -r src/* ${CATPDF}/
	echo "#!/usr/bin/env python3" > ${EXEC}
	echo workdir='"${CATPDF}/work/"' >> ${EXEC}
	cat ${CATPDF}/main.py >> ${EXEC}
	ln -s ${EXEC} ${INSTALL}/catpdf
	chmod 755 ${INSTALL}/catpdf

uninstall:
	unlink ${INSTALL}/catpdf
	rm -r ${CATPDF}


