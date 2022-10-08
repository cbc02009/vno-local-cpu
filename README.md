# template-container-image

Template for k8s-at-home containers. You can use it to as base to create your container.

The [.github](.github) folder will get PRs from this template so you can apply the latest workflows.

## How to use

This is a template so the resulting docker does not have any function. Here you should include the
instructions for your container or a link to the helm chart where it is used.

## Prereqs for GitHub workflows

You need to create the following secrets (not needed within the k8s-at-home org - there we use org-wide secrets):
- WORKFLOW_REPO_SYNC_TOKEN # Needed to do PRs that update the workflows
- GHCR_USERNAME # Needed to upload container to the Github Container Registry
- GHCR_TOKEN # Needed to upload container to the Github Container Registry

## How to build

1. Build and test local
    ```bash
    make
    ```
2. Build the container
    ```bash
    make docker-build
    ```

Check the [Makefile] for other build targets


