command=$1
branchname=$2
repository_ssh="git@github.com:yonghyeon0223/pynput_control_scripts.git"

if [[ $command == "push" ]]
then 
    if [[ $branchname == "" ]]
    then 
        echo -e "\nBranch has not been specified."
        echo -e "  Please pass in the name of your git branch as the second argument to the script.\n"
        exit;
    else
        echo ""
        branch_exits=` git branch | egrep "\W ${branchname}$" `
        if [[ $branch_exits != "" ]]
        then
            echo "branch exists"
            echo "  pushing to ${repository_ssh} ..."
            git push $repository_ssh $branchname
        else
            echo -e "Branch $branchname does not exist."
            echo -e "Instead, we have following branches available in this repository"
            git branch
        fi
        echo ""
    fi

elif [[ $command == "pull" ]]
then
    echo -e "\nPulling from $repository_ssh ..."
    git pull $repository_ssh
    echo ""

elif [[ $command == "commit" ]]
then
    read -p "Enter commit message: " commitMsg
    git commit -a -m "$commitMsg"
fi


