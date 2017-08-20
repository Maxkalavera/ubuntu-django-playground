# -*- mode: ruby -*-
# vi: set ft=ruby :

# In case ENV variables needed
# File.readlines('./conf/.env').each do |line|
#     key, value = line.split "="
#     ENV[key] = value
# end


Vagrant.configure('2') do |config|
	config.vm.box = 'ubuntu/trusty32'
	config.vm.box_url = 'https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-i386-vagrant-disk1.box'
  config.vm.network 'forwarded_port', guest: 8000, host: 8000
	config.ssh.forward_agent = true
	config.vm.synced_folder '.', '/home/vagrant/workspace/', create: true
	config.vm.provision 'shell' do |s|
    s.inline = '. ./install/install.sh $1'
    s.args   = ['install-dependencies']
  end

end