import requests
import time
import re
from cfg import mask, parser, wait

# проверка url
def urls_validate(url)->bool:

    if not re.match(mask, url):
        print(f"{url} - Невалидный")
        return False
    return True

# тест хостов
def hosts_test(url, count)->dict:

    info = {
        'Host': url,
        'Success': 0,
        'Failed': 0,
        'Errors': 0,
        'Times': []
    }


    for _ in range(count):
        try:
            start = time.time()
            answer = requests.get(url, timeout=wait)
            info['Times'].append((time.time() - start) * 1000)
            info['Success' if answer.status_code < 400 else 'Failed'] += 1
        except requests.exceptions.RequestException:
            info['Errors'] += 1
    info['Min'] = min(info['Times'])
    info['Max'] = max(info['Times'])
    info['Avg'] = sum(info['Times']) / len(info['Times'])
    return info

# вывод результата в консоль или в файл
def stats_output(info, output=None):

    result = f"""
{'#' * 50}
Host: {info['Host']}
Success: {info['Success']}
Failed: {info['Failed']}
Errors: {info['Errors']}
Min: {info['Min']:.2f} ms
Max: {info['Max']:.2f} ms
Avg: {info['Avg']:.2f} ms
{'#' * 50}
"""

    if output:
        with open(output, 'a') as f:
            f.write(result)
    else:
        print(result)


def main():

    args = parser()


    urls = []
    if args.hosts:
        urls = args.hosts.split(',')
    else:
        with open(args.file) as f:
            urls = [line.strip() for line in f if line.strip()]


    valid_urls = []
    for url in urls:
        if urls_validate(url):
            valid_urls.append(url)

    for url in valid_urls:
        stats = hosts_test(url, args.count)
        stats_output(stats, args.output)

if __name__ == '__main__':
    main()
