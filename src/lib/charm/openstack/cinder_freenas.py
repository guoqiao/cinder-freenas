import charms_openstack.charm
import charmhelpers.core.hookenv as ch_hookenv  # noqa

charms_openstack.charm.use_defaults('charm.default-select-release')


class CinderFreeNASCharm(
        charms_openstack.charm.CinderStoragePluginCharm):

    name = 'cinder_freenas'
    version_package = 'python-cinder-freenas'
    release = 'ocata'
    packages = [version_package]
    stateless = True
    # Specify any config that the user *must* set.
    mandatory_config = []

    def cinder_configuration(self):
        volume_driver = ''
        driver_options = [
            ('volume_driver', volume_driver),
            # Add config options that needs setting on cinder.conf
        ]
        return driver_options


class CinderFreeNASCharmRocky(CinderFreeNASCharm):

    # Rocky needs py3 packages.
    release = 'rocky'
    version_package = '2'
    packages = [version_package]
