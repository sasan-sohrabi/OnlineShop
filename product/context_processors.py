from order.models import OrderedProduct, Ordered


def add_variable_to_context(request):
    if str(request.user) != 'AnonymousUser':
        context = {
            'orderItem_total': OrderedProduct.objects.filter(order_id__customer_id__user=request.user).filter(
                order_id__complete=False),
            'order': Ordered.objects.get(customer_id__user=request.user, complete=False)
        }
        # for item in context['order']:
        #     print('---------------------------------------')
        #     print(item.to)

        print(context['order'])
        # item = context['order'].total_value_cart()
        # print(item)
        return context

    context = {'test': 'Hello'}
    return context
