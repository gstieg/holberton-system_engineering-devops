# **0x0A Configuration management**

# **Resources**

**Read or watch:**

        * Intro to Configuration Management
        * Puppet resource type: file (check “Resource types” for all manifest types in the left menu)
        * Puppet’s Declarative Language: Modeling Instead of Scripting
        * Puppet lint
        * Puppet emacs mode

# **Requirements**

**General**

	* All your files will be interpreted on Ubuntu 14.04 LTS
	* All your files should end with a new line
	* A README.md file at the root of the folder of the project is mandatory
	* Your Puppet manifests must pass puppet-lint without any errors
	* Your Puppet manifests must run without error
	* Your Puppet manifests first line must be a comment explaining what the Puppet manifest is about
	* Your Puppet manifests files must end with the extension .pp
# **Tasks**

**#0**

Using Puppet, create a file in /tmp.

Requirements:

File path is /tmp/holberton
File permission is 0744
File owner is www-data
File group is www-data
File contains I love Puppet

**#1**

Using Puppet, install puppet-lint.

Requirements:

Install puppet-lint
Version must be 2.1.1

**#3**

Using Puppet, create a manifest that kills a process named killmenow.

Requirements:

Must use the exec Puppet resource
Must use pkill
