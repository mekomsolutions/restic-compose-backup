FROM busybox
ADD ./testapp-entrypoint.sh testapp-entrypoint.sh
ENTRYPOINT []
CMD [ "./testapp-entrypoint.sh" ]