sudo apt-get -y install software-properties-common aptitude git python-simplejson
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get -y install ansible

cd ~
mkdir -p code
cd code
git clone https://github.com/theotheu/ebig-provisioning.git
cd ansible-ubuntu-desktop

ansible-playbook setup.yml --ask-sudo-pass --module-path ./ansible_modules --limit "$(hostname)"

exit 0