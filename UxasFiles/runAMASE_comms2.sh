SCRIPT_DIR="$( cd "$(dirname "$0")" ; pwd -P )"

cd "$AMASE_PATH";
java -Xmx2048m -splash:./data/amase_splash.png -classpath ./dist/*:./lib/*  avtas.app.Application --config config/amase --scenario "$SCRIPT_DIR/Scenario_comms2.xml";
cd "$SCRIPT_DIR";

