echo -E "Setting up all requirements"
echo -E "Installing all required packages"
python3 -m pip install -r requirements.txt
if [ $? -eq 0 ]; then
    echo -E "All requirements installed successfully"
else
    echo -E "Failed to install requirements. You must be on python3, and use windows. For ubuntu users, please use ubuntu_setup.sh"
    exit 1
fi