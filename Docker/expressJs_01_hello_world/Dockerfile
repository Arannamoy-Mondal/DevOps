FROM node:slim
RUN npm install -g pnpm
WORKDIR /app
RUN pnpm config set node-linker hoisted
COPY package.json pnpm-lock.yaml* ./
RUN pnpm install
COPY . .
EXPOSE 3000
ENTRYPOINT [ "node", "index.js" ]