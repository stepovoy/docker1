FROM ruby:latest
RUN apt-get update -y && && apt-get upgrade -y && apt-get install -y nodejs --no-install-recommends && \
	gem install rails && gem install bundler && gem install rake && mkdir -p /app
ONBUILD COPY . /app
ONBUILD WORKDIR /app
ONBUILD EXPOSE 3000
ONBUILD RUN rails new . && bundle && rake db:migrate --trace && rake db:seed --trace
