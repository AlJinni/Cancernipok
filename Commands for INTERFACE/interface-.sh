read -p ":"
if [ $REPLY == "l" ]; then
	bash ListFile.sh
fi
if [ $REPLY == "d" ]; then
	bash DeletionFile.sh
fi
if [ $REPLY == "r" ]; then
	bash RunningFiles.sh
fi
if [ $REPLY == "k" ]; then
	bash KillFile.sh
fi

bash interface-.sh
