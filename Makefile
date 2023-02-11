MAKEFLAGS += -s
clean:
	@rm *.tgz
	@echo 'Cleanup done!'
tgz:
	@tar --exclude=*.swp \
	     -czf zypper-onlinesearch-$(shell grep 'man 8' './zypper-onlinesearch/zypper-onlinesearch.8' | cut -f 4 -d '"').tgz ./zypper-onlinesearch
	@echo 'Archive ready!'
install:
	@sudo install -m 755 ./zypper-onlinesearch/zypper-onlinesearch /usr/lib/zypper/commands/
	@sudo install -m 644 ./zypper-onlinesearch/zypper-onlinesearch.8 /usr/share/man/man8/
	@echo 'Plugin installed!'
uninstall:
	@sudo rm /usr/lib/zypper/commands/zypper-onlinesearch || true
	@sudo rm /usr/share/man/man8/zypper-onlinesearch.8.gz || true
	@echo 'Plugin uninstalled!'
