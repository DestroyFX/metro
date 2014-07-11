from .chroot import ChrootTarget

class StageTarget(ChrootTarget):
    def __init__(self, settings):
        ChrootTarget.__init__(self, settings)

        # stages need a snapshot to install packages
        self.required_files.append("path/mirror/snapshot")

        # define gentoo specific mounts
        if "path/distfiles" in self.settings:
            self.mounts["/usr/portage/distfiles"] = self.settings["path/distfiles"]

        # let's bind-mount our main system's device nodes in place
        #if self.settings["portage/ROOT"] != "/":
            # this seems to be needed for libperl to build (x2p) during stage1
        #    self.mounts["/dev"] = "/dev"
        #    self.mounts["/dev/pts"] = "/dev/pts"

    def run(self):
        ChrootTarget.run(self)

        # now, we want to clean up our build-related caches, if configured to do so:
        if "metro/options" in self.settings:
            if "clean/auto" in self.settings["metro/options"].split():
                if "path/cache/build" in self.settings:
                    self.clean_path(self.settings["path/cache/build"])

# vim: ts=4 sw=4 et
