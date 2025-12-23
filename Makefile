INSTALL=${HOME}/PythonLib/lib

MERGE_DIR=${INSTALL}/merge_pdf
EXEC=${MERGE_DIR}/merge

.PHONY: install uninstall mkbash

install : 
	mkdir ${MERGE_DIR}
	mkdir ${MERGE_DIR}/latex
	mkdir ${MERGE_DIR}/work
	cp -r src/* ${MERGE_DIR}/
	echo "#!/usr/bin/env python3" > ${EXEC}
	echo workdir='"${MERGE_DIR}/work/"' >> ${EXEC}
	cat ${MERGE_DIR}/main.py >> ${EXEC}
	ln -s ${EXEC} ${INSTALL}/merge
	chmod 755 ${INSTALL}/merge

uninstall:
	unlink ${INSTALL}/merge
	rm -r ${MERGE_DIR}


