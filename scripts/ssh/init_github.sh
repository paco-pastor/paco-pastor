eval "$(ssh-agent)"
ssh-add ~/.ssh/github
echo -e 'Github initialized. Try \033[1mgit pull\033[1m, \033[1mgit push\033[0m or \033[1mgit clone\033[1m.'
