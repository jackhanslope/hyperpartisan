#!/usr/bin/env fish

if count $argv > /dev/null
    if test $argv[1] = "dev"
        echo "Installing dev"
        .venv/bin/pip install -r requirements/dev.txt -f https://download.pytorch.org/whl/torch_stable.html
    else if test $argv = "common"
        echo "Installing common"
        .venv/bin/pip install -r requirements/common.txt -f https://download.pytorch.org/whl/torch_stable.html
    else
        echo $argv[1] is not an option
    end
else
    echo No argument provided
end
