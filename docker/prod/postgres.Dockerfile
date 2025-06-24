FROM postgres:latest

# entrypoint
COPY entrypoints/prod/postgres-entrypoint.sh /usr/local/bin/entrypoints/postgres-entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoints/postgres-entrypoint.sh

# env
COPY env/prod/postgres-env.sh /etc/postgres/postgres-env.sh
RUN chmod +x /etc/postgres/postgres-env.sh

ENTRYPOINT ["/usr/local/bin/entrypoints/postgres-entrypoint.sh"]

CMD ["postgres"]