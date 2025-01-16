function postedBy(parent, args, context) {
  const { id } = parent;
  return context.prisma.link.findUnique({ where: { id } }).postedBy();
}

module.exports = {
  postedBy,
};
