# nullbeat-api

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

nullbeat-api is the API component of the nullbeat project, providing a command and control backend for the Minecraft Bots.

## Endpoints

- Items to storage all characters' inventories.
- Jobs to identify tasks and their ordered execution for the bots.
- Character call to identify users
- Statistics for overall usage.

Details on the endpoints specifcally are available via the built-in interface at the /docs endpoint of the site.

## Getting Started

### Prerequisites

Although this API does not depend on it, the propigator for this content is Nullbeat itself.

- [nullbeat](https://github.com/TargetedEntropy/nullbeat)

### Installation

1. Clone the nullbeat-api repository:

    ```bash
    git clone https://github.com/TargetedEntropy/nullbeat-api.git
    cd nullbeat-api
    ```

2. Configure your database backend. Tables are auto-generated.
    ```
    cp app/db/env.sample app/db/.env
    vi app/db/.env
    ```

    An example local sqlite endpoint would be defined as:
    ```
    SQLALCHEMY_DATABASE_URI=sqlite:///test.db
    ```
3. Start the application
    ```
    bash start.sh
    ```
