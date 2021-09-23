# export ENVIRONMENT=${1:-local}

# Gets the project home directory, a parent of devops repository.
if [ -z ${PROJ_HOME} ]; then
    export PROJ_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )/.." && pwd )";
fi

export VIRTUAL_ENV="env_django_google_authentication"


# Environment for prompt
FG_GREEN="\033[32m"
FG_BLACK="\033[00m"
FG_BLUE="\033[34m"
FG_ENVIRONMENT=${FG_GREEN}
FG_NORMAL="${FG_BLACK}"


###############################################################################################
# Helper scripts for printing
###############################################################################################

function print_message() {
    echo -e "${FG_BLUE}-------------------------------------------------------------------------------
    $@
-------------------------------------------------------------------------------${FG_NORMAL}"
}

function print_helper() {
    echo -e "${FG_GREEN}------------------------------------------------------------------------------
    $@
-------------------------------------------------------------------------------${FG_NORMAL}"
}

###############################################################################################
# Helper scripts for API
###############################################################################################
function api-build() {
    print_message "Building docker image ..."

    local build_image="social-authentication"
    docker build -t "${build_image}" .
}


function api-start() {
    local flag=$1

    print_message "Running api server ..."

    rm -rf celerybeat.pid

    if [ "${flag}" = "--build" ]; then
        docker-compose -f docker-compose.yml up --build
    else
        docker-compose -f docker-compose.yml up
    fi
}


function api-exec() {
    local service_name="api"

    print_message "Exec to docker container of API ..."
    docker-compose exec "$service_name" sh
}


function api-shell() {
    local service_name="api"

    print_message "Shell ..."
    docker-compose exec $service_name sh bin/dj-shell.sh
}


function banner() {
    print_message "Social Authentication"
    print_helper "Go with command: api-start"
}

banner