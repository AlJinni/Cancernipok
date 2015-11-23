read -p "
This is the INTERFACE, Master of the Tools of Terminal Cancer.
For ListFile, press l.
For DeletionFile, press d.
For RunningFiles, press r.
For KillFile, press k.
In an emergency, type KILL.
: ";
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
if [ $REPLY == "KILL" ]; then
	bash Emergencies.sh
fi


bash interface-.sh
