"""Version constant shared by the release tooling."""

VERSION = "1.4.0"


def artifact_name(name="acme-release-skills"):
    return f"{name}-{VERSION}.tar.gz"
